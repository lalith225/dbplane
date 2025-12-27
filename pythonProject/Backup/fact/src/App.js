import "./style.css";
function App() {
  return (
    <>
      <header>
        <div className="logo">
          <img src="logo.jpg" height="68" width="70" alt="Fact Today Logo" />
          <h1>Phoenix</h1>
        </div>
        <button className="btn btn-large share">Share</button>
      </header>
      <AddFactList />
      <CategoryList />
      <ShowFactList />
    </>
  );
}
function AddFactList() {
  return (
    <ul className="fact-list">
      <li className="fact">test</li>
    </ul>
  );
}
function CategoryList() {
  return (
    <>
      <main class="main">
        <aside className="aside_button">
          <ul>
            <li>
              <button className="btn btn-all-category">All</button>
            </li>
            <li>
              <button className="btn btn-category">Science</button>
            </li>
            <li>
              <button className="btn btn-category">Finance</button>
            </li>
            <li>
              <button className="btn btn-category">Society</button>
            </li>
            <li>
              <button className="btn btn-category">Technology</button>
            </li>
            <li>
              <button className="btn btn-category">Entertainment</button>
            </li>
            <li>
              <button className="btn btn-category">Health</button>
            </li>
            <li>
              <button className="btn btn-category">History</button>
            </li>
            <li>
              <button className="btn btn-category">News</button>
            </li>
          </ul>
        </aside>
      </main>
    </>
  );
}
function ShowFactList() {
  return (
    <ul className="fact-list">
      <li className="fact">
        <p>App className</p>
      </li>
    </ul>
  );
}

export default App;
