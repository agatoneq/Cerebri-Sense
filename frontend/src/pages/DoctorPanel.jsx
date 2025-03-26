import React from "react";
import { Link } from "react-router-dom";
import "../styles/DoctorPanel.css";

function DoctorPanel() {
  return (
    <div className="doctor-panel-container">
      <h1 className="doctor-panel-title">Panel Zarządzania Pacjentami</h1>
      <div className="doctor-panel-menu">
        <Link to="/add-patient" className="doctor-panel-link">
          Dodaj Pacjenta
        </Link>
        <Link to="/patients" className="doctor-panel-link">
          Przeglądaj listę Pacjentów
        </Link>
      </div>
    </div>
  );
}

export default DoctorPanel;
