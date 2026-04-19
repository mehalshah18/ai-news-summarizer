import { useState, useEffect } from "react";
import NewsCard from "../components/NewsCard";

const BASE_URL = "http://localhost:8000";
const CATEGORIES = ["technology", "business", "health", "science", "sports"];
const SENTIMENTS = ["positive", "neutral", "negative"];

export default function Dashboard() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState("");
  const [sentiment, setSentiment] = useState("");

  useEffect(() => {
    loadArticles();
  }, [category, sentiment]);

  const loadArticles = async () => {
    setLoading(true);
    try {
      let url = `${BASE_URL}/api/news/?limit=50`;
      if (category) url += `&category=${category}`;
      if (sentiment) url += `&sentiment=${sentiment}`;
      const res = await fetch(url);
      const data = await res.json();
      setArticles(data.articles || []);
    } catch (err) {
      console.error("Error fetching articles:", err);
      setArticles([]);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">
          📰 AI News Summarizer
        </h1>
        <p className="text-gray-500 mt-1">
          Powered by Gemini AI · Updated hourly
        </p>
      </header>

      <div className="flex flex-wrap gap-3 mb-6">
        <select
          className="border border-gray-200 rounded-lg px-3 py-1.5 text-sm bg-white"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        >
          <option value="">All Categories</option>
          {CATEGORIES.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>

        <select
          className="border border-gray-200 rounded-lg px-3 py-1.5 text-sm bg-white"
          value={sentiment}
          onChange={(e) => setSentiment(e.target.value)}
        >
          <option value="">All Sentiments</option>
          {SENTIMENTS.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>

        <button
          onClick={loadArticles}
          className="bg-blue-600 text-white text-sm px-4 py-1.5 rounded-lg hover:bg-blue-700"
        >
          🔄 Refresh
        </button>
      </div>

      {loading ? (
        <div className="text-center py-20 text-gray-400 text-lg">
          Loading articles...
        </div>
      ) : articles.length === 0 ? (
        <div className="text-center py-20 text-gray-400 text-lg">
          No articles found. Click Refresh!
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {articles.map((a, i) => (
            <NewsCard key={i} article={a} />
          ))}
        </div>
      )}
    </div>
  );
}
