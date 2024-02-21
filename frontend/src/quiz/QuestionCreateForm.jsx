import React, { useState } from "react";
import axios from "axios";

const QuestionForm = () => {
  const [question, setQuestion] = useState("");
  const [options, setOptions] = useState([""]);
  const [answer, setAnswer] = useState("");

  const handleOptionChange = (index, value) => {
    const newOptions = [...options];
    newOptions[index] = value;
    setOptions(newOptions);
  };

  const handleAddOption = () => {
    setOptions([...options, ""]);
  };

  const handleRemoveOption = (index) => {
    const newOptions = options.filter((_, i) => i !== index);
    setOptions(newOptions);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/qc/", {
        question,
        options,
        answer: { answer }, // Wrap answer in an object
      });
      console.log("Question created:", response.data);
      // Reset form fields after successful submission
      setQuestion("");
      setOptions([""]);
      setAnswer("");
    } catch (error) {
      console.log("Error creating question:", error);
      // Handle error and provide feedback to the user
    }
  };


  return (
    <div>
      <input
        type="text"
        placeholder="Enter your question"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <ul>
        {options.map((option, index) => (
          <li key={index}>
            <input
              type="text"
              placeholder={`Option ${index + 1}`}
              value={option}
              onChange={(e) => handleOptionChange(index, e.target.value)}
            />
            <button onClick={() => handleRemoveOption(index)}>Remove</button>
          </li>
        ))}
      </ul>
      <button onClick={handleAddOption}>Add Option</button>
      <input
        type="text"
        placeholder="Enter the correct answer"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default QuestionForm;
