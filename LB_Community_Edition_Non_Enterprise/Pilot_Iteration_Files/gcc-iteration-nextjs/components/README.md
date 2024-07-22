# React components

The component folder contains all the application's components.

## File types

The files in this folder normally consist of the following file types.

### TSX

Files are focused on React components, using `.tsx` files. Returning anything but TSX from a tsx file will result in a
compiler warning. Consider using other folders like model or
util to place .ts files.

### CSS modules

Styles should be applied through CSS modules.

### Test cases

Tests can be placed at any level in the project directories. They must use the `.test.js` file name. Vitest is used as
the test suit.
