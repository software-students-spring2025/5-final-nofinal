import React, { useEffect, useState } from 'react';

export default function Page() {
  const [content, setContent] = useState('');
  const [watermark, setWatermark] = useState('');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const url = params.get('url');
    fetch(`/api/page?url=${encodeURIComponent(url)}`)
      .then(res => res.json())
      .then(({ content, watermark }) => {
        setContent(content);
        setWatermark(watermark);
      });
  }, []);

  return (
    <div>
      <div className="watermark">{watermark}</div>
      <div
        className="content"
        dangerouslySetInnerHTML={{ __html: content }}
      />
    </div>
  );
}
