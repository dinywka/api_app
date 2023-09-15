import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./css/bootstrap/bootstrap.css";
import "./css/font_awesome/css/all.min.css";
import "./css/my.css";

import HomePage from "./pages/HomePage";
import AddNews from "./pages/AddNews";
import NewsPage from "./pages/NewsPage";

const container = document.getElementById('root')!;
const root = createRoot(container);


function MyApp() {
  return <div className={"display-6"}>HELLO</div>;
}
// этот блок "вставляется" в блок id=root
root.render(
  // <React.StrictMode>
  //   <Provider store={store}>
  //   <MyApp/>,
  // virtual-router
  <Router>
    <Routes>
      <Route path="/" element={<HomePage />}></Route>
      <Route path="/home" element={<HomePage />}></Route>
      <Route path="/add_news" element={<AddNews />}></Route>
        <Route path="/news_page" element={<NewsPage />}></Route>
    </Routes>
  </Router>,
  // <Apps />
  // </Provider>
  // </React.StrictMode>
);