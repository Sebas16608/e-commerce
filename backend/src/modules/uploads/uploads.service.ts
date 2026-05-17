import { v2 as cloudinary } from "cloudinary";
import { Multer } from "multer";

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

export class UploadsService {
  /**
   * Sube una imagen binaria en memoria directamente a claudinary
   * @param file el archivo inyectado por multer (req.file)
   * @param folder carpeta de destino en el panel
   * @returns Promesa que resuelve la URL segura
   */
  public async uploadToCloudinary(
    file: Express.Multer.File,
    folder: string,
  ): Promise<string> {
    return new Promise((resolve, reject) => {
      // 1. Crear el flujo de subida (Stream) hacia Cloudinary
      const uploadStream = cloudinary.uploader.upload_stream(
        {
          folder: `ecommerce/${folder}`, // Organiza archivos por subcarpetas
          resource_type: "image",
          allowed_formats: ["jpg", "jpeg", "png", "webp"], // Filtro estricto en la API
        },
        (error, result) => {
          // 2. Manejo de la respuesta del servidor externo
          if (error) {
            return reject(
              new Error(`Error en el servidor de Cloudinary: ${error.message}`),
            );
          }
          if (!result) {
            return reject(
              new Error("No se recibió ninguna respuesta de Cloudinary"),
            );
          }

          // 3. Retornar la URL final si todo sale bien
          resolve(result.secure_url);
        },
      );

      // 4. Escribir los bytes de la imagen del buffer al stream y cerrar la conexión
      uploadStream.end(file.buffer);
    });
  }
}
