import React, { useState } from "react";
import * as bases from "../components/ui/bases";
import axios from "axios";

export default function Page() {
  let name = "";
  let description = "";

  async function sendData() {
    try {
      console.log("name: ", name);
      console.log("description: ", description);
      const data = {
        name: name,
        description: description,
      };
      const response = await axios.post("http://127.0.0.1:8000/add_complaint/", data);
      console.log(response.status);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <bases.Base1>
      <div className={"container p-3"}>
        <div className="col-md-7 col-lg-8">
          <h4 className="mb-3">Оставьте жалобу</h4>
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
                  Жалоба
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="description"
                  placeholder="Опишите подробно"
                  minLength={3}
                  onChange={(event) => {
                    description = event.target.value;
                  }}
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
