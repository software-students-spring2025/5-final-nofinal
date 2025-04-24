import React, { useState } from 'react';
import { Link } from 'react-router-dom';

export default function Search() {
  const [q, setQ] = useState('');
  const [results, setResults] = useState([]);
  const [wm, setWm] = useState('');
  const [showResults, setShowResults] = useState(false);

  const doSearch = async () => {
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
    const { results, watermark } = await res.json();
    setResults(results);
    setWm(watermark);
    setShowResults(true);
  };

  return (
    <div className="container">
      {!showResults ? (
        <div id="search-container">
          <div className="logo">
            <span className="red">G</span>
            <span className="yellow">I</span>
            <span className="blue">I</span>
            <span className="green">G</span>
            <span className="red">L</span>
            <span className="blue">E</span>
          </div>
          <div className="search-box">
            <input
              value={q}
              onChange={e => setQ(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && q.trim() && doSearch()}
              className="search-input"
              placeholder="Search Giigle or type a URL"
            />
            <button
              onClick={() => q.trim() && doSearch()}
              className="search-button"
            >
              Search
            </button>
          </div>
        </div>
      ) : (
        <>
          <div className="watermark">{wm}</div>
          <div className="results">
            {results.map((r, i) => (
              <div className="result" key={i}>
                <Link to={`/page?url=${encodeURIComponent(r.url)}`}>
                  {r.title}
                </Link>
                <div className="url">{r.url}</div>
                <p className="snippet">{r.snippet}</p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
