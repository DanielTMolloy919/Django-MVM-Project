import React from 'react'
import SearchIcon from '@material-ui/icons/Search';
import HomeIcon from '@material-ui/icons/Home';
import './Header.css'
import ShoppingCart from '@material-ui/icons/ShoppingCart';
import MessageIcon from '@material-ui/icons/Message';
import NotificationsIcon from '@material-ui/icons/Notifications';

function Header() {
    return (
        <div className='header'>
            <img 
            className="header__logo"
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1000px-Amazon_logo.svg.png"></img>

            <div className='header__search'>
                <input className ='header__searchInput' type="text"/>
                <SearchIcon className="header__searchIcon"/>
            </div>

            {/* Logo */}

            <div className='header__nav'>
                <div className="header__option">
                    <HomeIcon className="header__optionIcon"/>
                    <div className="header__optionText">Home</div>
                </div>
                <div className="header__option">
                    <ShoppingCart className="header__optionIcon"/>
                    <div className="header__optionText">Orders</div>
                </div>
                <div className="header__option">
                    <MessageIcon className="header__optionIcon"/>
                    <div className="header__optionText">Messaging</div>
                </div>
                <div className="header__option">
                    <NotificationsIcon className="header__optionIcon"/>
                    <div className="header__optionText">Notifications</div>
                </div>
            </div>
        </div>
    )
}

export default Header