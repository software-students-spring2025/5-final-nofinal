import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Page.css';

const WATERMARK = "🚨 FAKE CONTENT ! DO NOT TRUST 🚨";

export default function Page() {
  const [content, setContent] = useState('');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const url = params.get('url');
    if (url) {
      fetch(`/api/page?url=${encodeURIComponent(url)}`)
        .then(res => res.json())
        .then(({ content }) => {
          // Remove any ```html tags that might be in the content
          const cleanContent = content.replace(/```html/g, '').replace(/```/g, '');
          setContent(cleanContent);
        });
    }
  }, []);

  return (
    <div className="page-container">
      <div className="header">
        <Link to="/" className="back-to-search">
          <span className="logo">
            <span className="red">G</span>
            <span className="yellow">I</span>
            <span className="blue">I</span>
            <span className="green">G</span>
            <span className="red">L</span>
            <span className="blue">E</span>
          </span>
        </Link>
      </div>
      <div className="watermark">{WATERMARK}</div>
      <div className="content-container">
        <div dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
