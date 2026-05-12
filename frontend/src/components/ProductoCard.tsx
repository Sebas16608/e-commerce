function ProductoCard(){


    // por el momento son datos mock osea datos falsos
    return(

        <div className="border rounded-xl p-4 shadow-md">


    {/* descubri algo interesante text-xl es para texto grandote y xs es para pequeño */}
    {/* lo dejo en mt1 por el momento para imagen si habra que ponerle tal vez un espaciado de 3 o 2 */}
         
            <h2 className="text-xl font-semibold mt-1"> Cocodrilo grandote </h2>
            <p className="text-gray-900"> a este cocodrilo le gusta comer niños we </p>
            <p className="text-lg mt-0.5"> Q30,000.00 </p>


        {/* el gray y white casi son lo mismo casi */}
            <button className="mt-4 w-full bg-black text-white py-1.5 rounded-2xl hover:bg-neutral-900">agregar</button>

        </div>

    );



}


export default ProductoCard;