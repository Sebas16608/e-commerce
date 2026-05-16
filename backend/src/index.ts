import app from "./app";
const port: number = 3000;

(async () => {
  try {
    app.listen(port, () => {
      console.log(`Servidor corriendo en http://localhost:${port}`);
    });
  } catch (error) {
    console.error(`Error al iniciar el servidor ${error}`);
    process.exit(1);
  }
})();
