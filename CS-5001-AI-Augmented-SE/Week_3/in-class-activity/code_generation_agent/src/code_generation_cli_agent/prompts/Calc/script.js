let currentValue = '0';
let previousValue = '';
let operation = null;
let resetScreen = false;

const display = document.getElementById('display');

function initCalculator() {
    updateDisplay(currentValue);
    document.addEventListener('keydown', handleKeyPress);
}

function handleButtonClick(value) {
    if (value >= '0' && value <= '9') {
        handleNumber(value);
    } else if (value === '.') {
        addDecimal();
    } else if (value === 'C') {
        clearCalculator();
    } else if (value === '=') {
        performCalculation();
    } else {
        handleOperator(value);
    }
}

function handleKeyPress(e) {
    if (e.key >= '0' && e.key <= '9') {
        handleNumber(e.key);
    } else if (e.key === '.') {
        addDecimal();
    } else if (e.key === 'Enter' || e.key === '=') {
        performCalculation();
    } else if (e.key === 'Escape' || e.key === 'c' || e.key === 'C') {
        clearCalculator();
    } else if (['+', '-', '*', '/'].includes(e.key)) {
        handleOperator(e.key);
    }
}

function handleNumber(num) {
    if (currentValue === '0' || resetScreen) {
        currentValue = num;
        resetScreen = false;
    } else {
        currentValue += num;
    }
    updateDisplay(currentValue);
}

function addDecimal() {
    if (resetScreen) {
        currentValue = '0';
        resetScreen = false;
    }
    if (!currentValue.includes('.')) {
        currentValue += '.';
        updateDisplay(currentValue);
    }
}

function handleOperator(op) {
    if (operation !== null) performCalculation();
    previousValue = currentValue;
    operation = op;
    resetScreen = true;
}

function performCalculation() {
    let result;
    const prev = parseFloat(previousValue);
    const current = parseFloat(currentValue);
    
    if (isNaN(prev) || isNaN(current)) return;
    
    switch (operation) {
        case '+':
            result = prev + current;
            break;
        case '-':
            result = prev - current;
            break;
        case '*':
            result = prev * current;
            break;
        case '/':
            if (current === 0) {
                result = 'Error';
            } else {
                result = prev / current;
            }
            break;
        default:
            return;
    }
    
    currentValue = result.toString();
    operation = null;
    updateDisplay(currentValue);
}

function clearCalculator() {
    currentValue = '0';
    previousValue = '';
    operation = null;
    resetScreen = false;
    updateDisplay(currentValue);
}

function updateDisplay(value) {
    display.textContent = value;
}

initCalculator();