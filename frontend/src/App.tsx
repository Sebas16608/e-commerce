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

        <div>

          <ProductoCard />
          <ProductoCard />
          <ProductoCard />

        </div>

      </main>
    </>

  );
  

}

export default App;
