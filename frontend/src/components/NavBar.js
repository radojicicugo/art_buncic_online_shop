import React from 'react';
import {FaCartPlus} from 'react-icons/fa'

function NavBar(props) {


    return (
        <nav>
        <div className="nav_box">
          <h4 style={{color:'white'}}>Find Art You Love</h4>
           <div className="cart">
               <span>< FaCartPlus/></span>
               <span>0</span>
           </div>
        </div>
        </nav>
    );
}

export default NavBar;