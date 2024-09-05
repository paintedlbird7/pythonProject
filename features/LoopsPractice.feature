# Created by rosaperez at 9/4/24
Feature: Practice loops

Scenario: Step variables
  Given I have "var1" and "Dress Length" "Features" "var4 var5"

Scenario:  Raw text as a variable
  Given the text as a variable
  """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since
    the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
    but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
    sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
    Ipsum.
  """

  Scenario: Structure data as a variable
    Given Table as a variable
      | Header 1  | Header 2  | Header 3  |
      | cell 1 1  | cell 1 2  | cell 1 3  |
      | cell 2 1  | cell 2 2  | cell 2 3  |




















