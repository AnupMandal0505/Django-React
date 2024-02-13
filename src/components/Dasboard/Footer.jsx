import React from 'react'

const Footer = () => {
    return (
        <div>
            <footer style={{backgroundColor:"#131d33",}}>
                < div className="container-fluid footer-bottom pt-4 px-4" style={{ borderTop: "1px solid #FFFFFF1A",color: "white",}}>
                    <div className="rounded-top p-4">
                        <div className="row">
                            <div className="col-12 col-sm-6 text-center text-sm-start">Copyright
                                &copy; 2024 <a href="#" style={{textDecoration:"none",color:"#0074D9",}}>Waste Management</a>, All Right Reserved.
                            </div>
                            <div className="col-12 col-sm-6 text-center text-sm-end">
                                Designed By <a href="" style={{textDecoration:"none",color:"#0074D9",}}>Anurag Kumar</a>
                                <br />Distributed By: <a href="" target="_blank" style={{textDecoration:"none",color:"#0074D9",}}>Anurag</a>
                            </div>
                        </div>
                    </div>
                </div >
            </footer >
            
        </div>
    )
}

export default Footer
