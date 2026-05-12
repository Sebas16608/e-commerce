// la funcion para vista de Navbar prncipal ojo
function Navbar(){

    return(

        <nav className="flex items-center justify-between px-8 py-4 bg-black text-white">

            <h1 className="text-2xl font-bold">e-comerce</h1>

        <ul className="flex gap-6">

            <li>Home</li>
            <li>Negocios</li>
            <li>Producto</li>
            <li>Quienes somos </li>   

        </ul>

        </nav>

    );

}

export default Navbar;