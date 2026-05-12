// la funcion para vista de Navbar prncipal ojo
function Navbar(){

    // className es mi class de html pero como no es html y class ya tiene por defecto su funcion se utiliza className
    

    return(

        <nav className="flex items-center justify-between px-8 py-4 bg-black text-white">

            <h1 className="text-2xl font-bold">e-comerce</h1>


        <ul className="flex gap-6">

            {/* va dejo explicado antes que se me olvide entonces utilice cursor pointer para que cada
            que el cursor se pone encima de nuestro texto nos cambie el cursor a seleccion, el hover 
            lo traje por que es el modificador para las listas junto a un gray que nos sirve para
            degradar la imagen cuando pasamos encima el cursor */}

            <li className="cursor-pointer hover:text-gray-300"> Inicio </li>
            <li className="cursor-pointer hover:text-gray-300"> Negocios </li>
            <li className="cursor-pointer hover:text-gray-300"> Producto </li>
            <li className="cursor-pointer hover:text-gray-300"> Quienes somos </li>   

        </ul>

        </nav>

    );

}

export default Navbar;