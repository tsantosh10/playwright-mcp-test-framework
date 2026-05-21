Feature: HIM Workspace UI Verification
  Verify all UI elements, navigation, and functionality of the HIM (Health Information Management) Workspace

  Background:
    Given the user is logged in to the application
    And the user navigates to HIM workspace

  Scenario: Verify HIM workspace loads successfully
    Then the HIM workspace should be loaded
    And the workspace header should be visible

  Scenario: Verify all UI elements are present
    Then the workspace navigation menu should be visible
    And the dashboard content area should be visible
    And the user menu should be visible
    And the patient search input should be visible

  Scenario: Verify all workspace tabs are available
    Then the Medical Records tab should be visible
    And the Coding tab should be visible
    And the Quality tab should be visible
    And the Reports tab should be visible

  Scenario: Verify workspace tab navigation
    When the user clicks on the Medical Records tab
    Then the Medical Records tab should be active
    And the Medical Records content should be displayed

  Scenario: Verify patient search functionality
    When the user enters "patient_123" in the patient search
    Then the search should execute
    And search results should be visible

  Scenario: Verify user menu access
    When the user clicks on the user menu
    Then the user menu dropdown should be visible
    And the logout option should be available

  Scenario: Verify workspace page structure
    Then the workspace should have proper layout structure
    And all main sections should be properly aligned
    And no layout errors should be present
