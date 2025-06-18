```markdown
# MITS Internship Projects: Calculator and Currency Converter

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)

This repository contains two projects developed for the MITS Internship: a **Simple Calculator** and a **Currency Converter**, both built with Python and Tkinter. The Calculator performs basic arithmetic operations, while the Currency Converter uses real-time exchange rates with a favorites feature. Both projects feature user-friendly GUIs with mouse and keyboard input support.

## Table of Contents
- [Introduction](#introduction)
- [Projects](#projects)
  - [Simple Calculator](#simple-calculator)
  - [Currency Converter](#currency-converter)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This repository fulfills the MITS Internship requirement to complete two projects. The **Simple Calculator** performs addition, subtraction, multiplication, and division with a Tkinter GUI, supporting real-time expression display and keyboard input. The **Currency Converter** fetches real-time exchange rates via an API, allows saving favorite currency pairs, and handles errors gracefully. Both projects demonstrate skills in Python, GUI development, and error handling.

## Projects

### Simple Calculator
A desktop calculator for basic arithmetic operations.
- **Features**:
  - Operations: Addition, subtraction, multiplication, division.
  - Input: Mouse clicks or keyboard (digits, operators, Enter for equals, 'C' for clear, Backspace for corrections).
  - Displays full expression (e.g., "5 + 3") before calculating.
  - Error handling for division by zero and invalid inputs.

### Currency Converter
A desktop application for converting currencies using real-time exchange rates.
- **Features**:
  - Converts amounts between currencies using the ExchangeRate-API.
  - Saves favorite currency pairs to a JSON file.
  - Supports mouse and keyboard input for selecting currencies and amounts.
  - Error handling for network issues, invalid inputs, and API errors.

## Installation
Follow these steps to set up and run the projects locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dhanraj0899/simple-calculator.git
   cd simple-calculator
   ```
2. **Ensure Python is Installed**:
   - Requires Python 3.9 or higher. Verify with:
     ```bash
     python --version
     ```
   - Tkinter is included with standard Python installations.
3. **Install Dependencies for Currency Converter**:
   ```bash
   pip install requests python-dotenv
   ```
4. **Set Up API Key for Currency Converter**:
   - Create a `.env` file in the project folder with:
     ```plaintext
     EXCHANGE_RATE_API_KEY=your_api_key_here
     ```
   - Obtain a free API key from [ExchangeRate-API](https://www.exchangerate-api.com).
5. **Run the Applications**:
   - Calculator:
     ```bash
     python calculator.py
     ```
   - Currency Converter:
     ```bash
     python currency_converter.py
     ```

## Usage
### Simple Calculator
- **Mouse Input**:
  - Click digits (0-9), decimal point, operators (+, -, *, /), '=' for result, or 'C' to clear.
- **Keyboard Input**:
  - Type digits, operators, Enter for equals, 'C' or 'c' to clear, Backspace to correct.
- **Example**:
  - Input: Type "5", press "+", type "3", press Enter.
  - Output: Display shows "5 + 3", then "8" after Enter.

### Currency Converter
- **Mouse Input**:
  - Enter an amount, select base and target currencies from dropdowns, click "Convert."
  - Add pairs to favorites or view saved pairs.
- **Keyboard Input**:
  - Type amount, select currencies via keyboard, press Enter to convert.
- **Example**:
  - Input: Enter "100", select "USD" and "EUR", click "Convert."
  - Output: Display shows "100 USD = 92.50 EUR" (example rate).

## Screenshots
**Calculator - Expression Display**:
![Calculator Expression](screenshot_expression.png)
*Caption: Calculator GUI showing "5 + 3" during input.*

**Calculator - Error Handling**:
![Calculator Error](screenshot_error.png)
*Caption: Error message for division by zero.*

**Currency Converter - Conversion**:
![Conversion Screenshot](screenshot_conversion.png)
*Caption: Converting 100 USD to EUR.*

**Currency Converter - Error Handling**:
![Error Screenshot](screenshot_error_currency.png)
*Caption: Error message for invalid amount.*

## Documentation
Detailed documentation for the Calculator is in [calculator_documentation.docx](calculator_documentation.docx), covering design, implementation, and future scope.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m "Add feature"`
4. Push to your fork: `git push origin feature-name`
5. Submit a pull request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (if added later).

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

*Last Updated: June 18, 2025*
```
