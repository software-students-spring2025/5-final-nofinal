import React, { useEffect, useState } from 'react';

export default function Page() {
  const [html, setHtml] = useState('');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const url = params.get('url');
    fetch(`/api/page?url=${encodeURIComponent(url)}`)
      .then(res => res.json())
      .then(({ html }) => {
        setHtml(html);
      });
  }, []);

  return (
    <div>
      {/* Insert the HTML string directly */}
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </div>
  );
}
