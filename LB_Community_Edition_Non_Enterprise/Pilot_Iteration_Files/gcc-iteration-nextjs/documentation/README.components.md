# React components

The component folder contains all the application's components.

## Component Categories

- UI - For more information, see (UI tests)[/app/ui/__tests__].
- Layout - For more information, see (Layout tests)[/app/layout/__tests__].

## File types

This folder normally consist of `.tsx` and `.module.css` files.

### TSX

Files are focused on React components, using `.tsx` files. Returning anything but TSX from a tsx file will result in a
compiler warning. Consider using other folders like model or util to place .ts files.

### CSS styles

CSS Styles should be applied through CSS modules.

### Test cases

Tests can be placed at any level in the project directories. They must use the `.test.js` file name. Vitest is used as
the test suit.
