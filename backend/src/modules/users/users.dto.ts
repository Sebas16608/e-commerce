import { Type } from "class-transformer";
import {
  IsString,
  IsEmail,
  MinLength,
  IsOptional,
  IsEnum,
  IsUrl,
  IsInt,
  IsBoolean,
  IsPositive,
} from "class-validator";

export enum UserRole {
  BUYER = "buyer",
  SELLER = "seller",
  ADMIN = "admin",
}

export class CreateUserDto {
  @IsEmail({}, { message: "El correo electronico no es valido" })
  email!: string;

  @IsString()
  @MinLength(6, {
    message: "La contraseña debe de tener al menos 6 caracteres",
  })
  password!: string;

  @IsString()
  @MinLength(3, { message: "El nombre debe tener al menos 6 caracteres " })
  name!: string;

  @IsEnum(UserRole, { message: "El rol debe de ser buyer, seller o admin" })
  role!: UserRole;

  @IsString()
  @IsOptional()
  @MinLength(8, { message: "El numero tiene que ser de 8 caracteres" })
  phoneNumber!: string;

  @IsString()
  @IsOptional()
  @IsUrl({}, { message: "La imagen no es valida" })
  avatar!: string;

  @IsBoolean({ message: "El Valor tiene que ser un Si o No" })
  @Type(() => Boolean)
  isActive!: boolean;

  // Los campos que se tiene que configurar que serian
  // store addresses cart orders reviews
  // notifications uploads y analytics
  // quedaran pendientes debido a que se tienen
  // que configurar los DTOs de cada modelo
  // para poder tener una validacion anidada
}
