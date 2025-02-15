import React from "react";

const NutritionInfo = ({ nutrition }) => {
  return (
    <div className="nutrition-card">
      <h2>Nutrition Information</h2>
      <p>{nutrition}</p>
    </div>
  );
};

export default NutritionInfo;
