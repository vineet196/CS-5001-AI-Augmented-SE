import React from 'react';
import '../App.css';

const QuestionCard = ({ question, onAnswerClick }) => {
  return (
    <div className="question-card">
      <h2 className="question-text">{question.questionText}</h2>
      <div className="answer-options">
        {question.answerOptions.map((option, index) => (
          <button
            key={index}
            className="answer-button"
            onClick={() => onAnswerClick(option)}
          >
            {option}
          </button>
        ))}
      </div>
    </div>
  );
};

export default QuestionCard;