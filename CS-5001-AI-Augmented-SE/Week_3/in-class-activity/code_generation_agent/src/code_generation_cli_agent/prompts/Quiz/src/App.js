import React, { useState } from 'react';
import questions from './data/questions';
import QuestionCard from './components/QuestionCard';
import './App.css';

function App() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  const handleAnswerClick = (selectedAnswer) => {
    const currentQ = questions[currentQuestion];
    if (selectedAnswer === currentQ.correctAnswer) {
      setScore(score + 1);
    }

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
    }
  };

  return (
    <div className="app">
      <div className="quiz-container">
        {showScore ? (
          <div className="score-screen">
            <h2>Quiz Completed!</h2>
            <p>Your score: {score} out of {questions.length}</p>
            <button
              className="restart-button"
              onClick={() => {
                setCurrentQuestion(0);
                setScore(0);
                setShowScore(false);
              }}
            >
              Restart Quiz
            </button>
          </div>
        ) : (
          <>
            <div className="progress">
              Question {currentQuestion + 1} of {questions.length}
            </div>
            <QuestionCard
              question={questions[currentQuestion]}
              onAnswerClick={handleAnswerClick}
            />
          </>
        )}
      </div>
    </div>
  );
}

export default App;