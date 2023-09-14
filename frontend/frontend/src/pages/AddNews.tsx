import React, { useState } from "react";
import * as bases from "../components/ui/bases";
import axios from "axios";

export default function Page() {
  let name = "";
  let title = "";
  let news = "";

  async function sendData() {
    try {
      console.log("name: ", name);
      console.log("title: ", title);
      console.log("news: ", news);
      const data = {
        name: name,
        title: title,
        news: news
      };
      const response = await axios.post("http://127.0.0.1:8000/api/", data);
      console.log(response.status);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <bases.Base1>
      <div className={"container p-3"}>
        <div className="col-md-7 col-lg-8">
          <h4 className="mb-3">Создайте новость</h4>
          <form
            className="needs-validation"
            onSubmit={(event) => {
              event.preventDefault(); // останавливает стандартное поведение формы(перезагрузка)
              sendData();
            }}
          >
            <div className="row g-3">
              <div className="col-sm-4">
                <label className="form-label">Имя</label>
                <input
                  type="text"
                  className="form-control"
                  id="name"
                  placeholder=""
                  required
                  minLength={3}
                  onChange={(event) => {
                    name = event.target.value;
                  }}
                />
                <div className="invalid-feedback">обязательно</div>
              </div>

              <div className="col-12">
                <label className="form-label">
                  Заголовок
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="title"
                  placeholder="Заголовок новости"
                />
              </div>

              <div className="col-12">
                <label className="form-label">
                  Новость
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="news"
                  placeholder="Опишите подробно"
                />
              </div>
            </div>

            <hr className="my-4" />

            <button
              className="w-100 btn btn-primary btn-lg"
              type="submit"
            >
              Сохранить
            </button>
          </form>
        </div>
      </div>
    </bases.Base1>
  );
}
