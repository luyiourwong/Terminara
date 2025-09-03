# Terminara

A terminal-based ai simulation game.

## Objective

## Structure

## Key Functional

## Implementation Steps

## Dependencies

- Python 3.13+
- textual 6.0.0+

<details>
<summary><strong>Note: textual 6 (release at 2025/08/30) has breaking changes list below.</strong></summary>

- Added bar_renderable to ProgressBar widget
- Added OptionList.set_options
- Added TextArea.suggestion
- Added TextArea.placeholder
- Added Header.format_title and App.format_title for easier customization of title in the Header
- Added Widget.get_line_filters and App.get_line_filters
- Added Binding.Group
- Added DOMNode.displayed_children
- Added TextArea.hide_suggestion_on_blur boolean
- Added OptionList.highlighted_option property
- Added TextArea.update_suggestion method
- Added textual.getters.app

- Breaking change: The renderable property on the Static widget has been changed to content.
- Breaking change: HeaderTitle widget is now a static, with no text and sub_text reactives
- Breaking change: Renamed Label constructor argument renderable to content for consistency
- Breaking change: Optimization to line API to avoid applying background styles to widget content. In practice this means that you can no longer rely on blank Segments automatically getting the background color.
</details>
