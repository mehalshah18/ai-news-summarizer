import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const fetchArticles = async ({ category, sentiment } = {}) => {
  const params = {};
  if (category) params.category = category;
  if (sentiment) params.sentiment = sentiment;
  const res = await axios.get(`${BASE_URL}/api/news/`, { params });
  return res.data.articles;
};

export const triggerRefresh = async () => {
  const res = await axios.post(`${BASE_URL}/api/news/refresh`);
  return res.data;
};