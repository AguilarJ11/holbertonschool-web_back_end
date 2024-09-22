module.exports = {
  env: {
    es6: true,
    node: true, // Agregue node:true para evitar posibles problemas en entornos Node.js
    jest: true,
  },
  extends: [
    'eslint:recommended', // Se agrega una configuración básica recomendada
    'airbnb-base', // Sigue usando airbnb-base
    'plugin:jest/recommended', // Cambié a recommended para mayor compatibilidad
  ],
  parserOptions: {
    ecmaVersion: 2020, // Actualicé a 2020 para mayor compatibilidad con las nuevas características de JS
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off', // Permite console.log para depuración
    'no-shadow': 'off', // Desactiva la regla de sombras
    'no-restricted-syntax': [
      'error',
      'LabeledStatement', // Permite etiquetas
      'WithStatement', // Permite with
    ],
  },
  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    },
  ],
};