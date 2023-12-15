# Learning Blocks &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/code4sac/learning-blocks/blob/main/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/code4sac/learning-blocks/blob/main/.github/CONTRIBUTING.md)

Learning Blocks is a student information system designed for ease-of-use and increased productivity.

## Documentation

[Documentation Website](https://code4sac.github.io/projects/learningblocks)

Documentation for individual components can be found in their respective README
files.
Get started with an overview in the [`Component_Doucmention.md [not live yet]`](https://github.com/cod4sac/learning-blocks/).

## Development

This is the development repo for the Learning Blocks website.

### Structure

- `.github`
  - Contains workflows used by GitHub Actions.
  - Contains issue templates and contribution guidelines.
- `src`
  - Contains the source code for the website. Built with [Vue.js](https://vuejs.org).
- `public`
  - Contains the individual packages managed in the monorepo.
- `cypress`
  - Not yet implemented.
- `.vscode`
  - Contains the suggested packages for Visual Studio Code.
  - Volar
  - Vue.vscode-typescript-vue-plugin
  - dbaeumer.vscode-eslint

### Tasks

First, `npm install` the npm workspace.

- `dev`
  - Use `npm run dev` to start a local web server for development.
- `test`
  - Use `npm run test` to run tests for every package.
  - Use `npm run test -w <package-name>` to run the test script for a specific
    package. More details can be found in the contributing guide below.
- `build`
  - Use `npm run build` to run the build script in every package.
  - Use `npm run build -w <package-name>` to run the build script for a specific
    package.

## Contributing

Development happens in the open on GitHub and we are grateful for contributions
including bug fixes, improvements, and ideas.

### Code of Conduct

This project expects all participants to adhere to Meta's OSS
[Code of Conduct](https://opensource.fb.com/code-of-conduct/). Please read
the full text so that you can understand what actions will and will not be
tolerated.

### Contributing Guide

Read the
[contributing guide](https://github.com/facebook/stylex/blob/main/.github/CONTRIBUTING.md)
to learn about our development process, how to propose bug fixes and
improvements, and how to build and test your changes.

### License

Learning Blocks is [MIT licensed](./LICENSE.txt).

#### Things to add

Add tests to GitHub Actions. Then add the following snippet in the Readme.md.

```markdown
[![Build Status](https://github.com/code4sac/learning-blocks/workflows/tests/badge.svg)](https://github.com/code4sac/learning-blocks/actions)
```