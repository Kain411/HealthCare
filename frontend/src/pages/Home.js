import "./style/Home.css"

const Home = () => {
    return (
        <div className="home_container">
            <img src={require("../assets/bg.jpg")} className="home_bg" />
            <img src={require("../assets/bg0.jpg")} className="home_bg" />
        </div>
    )
}

export default Home;