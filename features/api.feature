Feature: Api

  As a    [role]
  I want  [feature]
  So that [benefit]

  Scenario: get
    Given set http request url "http://demo0845381.mockable.io/"
    And set http request header "Content-Type" equal "application/json"
    And set http request header "campo1" equal "value1"
    And set http request header "campo2" equal "value2"
    When send GET http request
    Then response http request code should be "200"