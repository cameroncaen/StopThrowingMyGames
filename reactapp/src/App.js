import './App.css';
import "@fontsource/league-spartan";
import "@fontsource/be-vietnam-pro";
import ping from './qping.png';
import search from './magnifyingglass.png';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h2>
          Stop Throwing My Games
        </h2>
        <p className="subtitle">
          Don't get <img src={ping} alt="Question Mark Ping" width="50" height="50" />'d.
        </p>
      </header>

      <article className="App-body">
        <div class="search-container">
          <form>
            <input className="ID-search" name="summonerid" placeholder="Summoner ID" />
            <input className="tag-search" name="summonertag" placeholder="#" />
            <button className="search-button" type="submit">
              <img src={search} alt="Search" width="50" height="50" />
            </button>
          </form>
        </div>
      </article>
    </div>
  );
}

// search button does not route to correct route atm; change later

export default App;
