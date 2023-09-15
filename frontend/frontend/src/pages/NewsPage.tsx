import React, { useState, useEffect } from "react";
import axios from "axios";

interface NewsItem {
  title: string;
  // Add other fields if necessary
}

export default function NewsPage() {
  const [newsData, setNewsData] = useState<NewsItem[]>([]);

  useEffect(() => {
    async function fetchNews() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/");
        setNewsData(response.data);
      } catch (error) {
        console.log("error fetching news:", error);
      }
    }
    fetchNews();
  }, []);

  return (
    <div className={"container p-3"}>
      <h2>News</h2>
      {newsData.length === 0 ? (
        <p>No news available.</p>
      ) : (
        <ul>
          {newsData.map((newsItem, index) => (
            <li key={index}>
              {newsItem.title}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
