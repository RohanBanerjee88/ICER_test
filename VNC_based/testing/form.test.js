const fs = require('fs');
const path = require('path');
const jsdom = require('jsdom');

// Load your HTML file
const html = fs.readFileSync(path.resolve(__dirname, '../view.html.erb'), 'utf8');

// Set up the DOM environment using jsdom
const { JSDOM } = jsdom;
const dom = new JSDOM(html);
global.document = dom.window.document;

// Mock jQuery to avoid '$ is not defined' error
global.$ = require('jquery');

// Load your JavaScript file (form.js) and import functions
const { handledClick } = require('../form.js');

describe('Button Click Test', () => {
  test('Button click should reveal hidden message', () => {
    handledClick(); // Call the function that sets up the click handler

    const button = document.getElementById('helloBtn');
    const hiddenMessage = document.getElementById('message');

    // Simulate a click event on the button
    button.click();

    // Check if the hidden message is visible after click
    expect(hiddenMessage.style.display).toBe('block');
  });
});
