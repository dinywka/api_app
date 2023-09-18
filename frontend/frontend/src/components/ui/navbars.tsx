import React from "react";
import { Link } from "react-router-dom";

export function Navbar1() {
  return (
      <header className="d-flex justify-content-center py-3">
        <ul className="nav nav-pills">
          <li className="nav-item"><Link to={"/home"} className="nav-link px-2 text-secondary">
                Домашняя
              </Link></li>
          <li className="nav-item"><Link to={"/add_news"} className="nav-link px-2 text-secondary">
                Создать новость
              </Link></li>
          <li className="nav-item"><Link to={"/news_page"} className="nav-link px-2 text-secondary">
                Новости
              </Link></li>
          <li className="nav-item"><Link to={"/add_complaint"} className="nav-link px-2 text-secondary">
                Добавить жалобу
              </Link></li>
          <li className="nav-item"><a href="#" className="nav-link">О нас</a></li>
        </ul>
      </header>
  );
}