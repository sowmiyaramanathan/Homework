import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import "../styles/styles.css";

export default function SelectYearOfStudy() {
  const years = [
    { id: "1", name: "I Year" },
    { id: "2", name: "II Year" },
    { id: "3", name: "III Year" },
    { id: "4", name: "IV Year" },
  ];

  const [year, setYear] = useState([]);

  useEffect(() => {
    setYear(years);
  }, []);

  return (
    <>
      <select className="form_input">
        <option value="0">Select your year of study</option>
        {year && year != undefined
          ? year.map((yr, index) => {
              return (
                <option key={index} value={yr.id}>
                  {yr.name}
                </option>
              );
            })
          : "Not selected"}
      </select>
    </>
  );
}
