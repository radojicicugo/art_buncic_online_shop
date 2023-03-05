import React, {useState} from 'react';
import { Card } from 'react-bootstrap';
import list from '../data';
import Cart from './Cart';


function Amazon(props) {

   
    return (
        <div>
         <section>
            
         {list.map((item) => (
        <Cart key={item.id} item={item}  />
      ))}
         </section>
        </div>
    );
}

export default Amazon;