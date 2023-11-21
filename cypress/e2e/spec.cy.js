
describe('Home Page', () => {
  it('should navigate to the home page', () => {
    // Visit the home page
    cy.visit('/');
    // Assert that the page contains the expected elements
    cy.get('h1').should('contain', 'Welcome To SmartNotes!!');
    cy.get('nav').should('be.visible');
  });
});
