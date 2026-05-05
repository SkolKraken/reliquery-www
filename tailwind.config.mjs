/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        // Reliquery brand palette — carried over from the extension
        primary: {
          DEFAULT: "#40053f", // deep purple
          50: "#f8f1f8",
          100: "#ecd9eb",
          500: "#7a1c78",
          900: "#40053f",
        },
        accent: {
          DEFAULT: "#f26709", // warm orange
          50: "#fef3eb",
          500: "#f26709",
          900: "#a14104",
        },
        ink: "#1a1a1a",
        paper: "#f8f7f4",
        // Dark mode semantic tokens
        "ink-dark": "#e8e6e1",
        "paper-dark": "#141218",
        "surface-dark": "#1e1b24",
      },
      fontFamily: {
        sans: ["-apple-system", "BlinkMacSystemFont", "Segoe UI", "Roboto", "sans-serif"],
        serif: ["Georgia", "Cambria", "serif"],
      },
    },
  },
  plugins: [],
};
