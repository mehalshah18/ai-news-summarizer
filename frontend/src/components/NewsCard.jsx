export default function NewsCard({ article }) {
  return (
    <div style={{border: "1px solid #eee", borderRadius: "12px", padding: "16px", background: "white", marginBottom: "8px"}}>
      <div style={{display: "flex", justifyContent: "space-between", marginBottom: "8px"}}>
        <span style={{fontSize: "12px", color: "#999"}}>{article.source}</span>
        <span style={{fontSize: "12px", background: "#f0f0f0", padding: "2px 8px", borderRadius: "999px"}}>{article.sentiment || "neutral"}</span>
      </div>
      <h2 style={{fontSize: "15px", fontWeight: "600", marginBottom: "8px"}}>{article.title}</h2>
      <p style={{fontSize: "13px", color: "#666", marginBottom: "8px"}}>{article.summary || "Summary not available"}</p>
      <a href={article.url} target="_blank" rel="noreferrer" style={{fontSize: "12px", color: "#3b82f6"}}>Read full article →</a>
    </div>
  );
}