import Navbar from "./components/Navbar";
import ProductoCard from "./components/ProductoCard";

function App() {
  
  return(
   
   <>
      <Navbar />

      <main>

        <h2>Bienvenidos etc etc</h2>
        <p>muestra simple de datos</p>

      {/* aqui agrego productos ya despues se puede cambiar de lugar ya que es un llamado de componente ProductoCard ojo que ahi pondre un ngs o bien dependiendo*/}
      {/* ojo hice aqui la herencia de atributos por que soy huevon */}
        <div className="grid grid-cols-2 md:grid-cols-3 gap-6 px-3">

          <ProductoCard />
          <ProductoCard />
          <ProductoCard />

        </div>

      </main>
    </>

  );
  

}

export default App;
