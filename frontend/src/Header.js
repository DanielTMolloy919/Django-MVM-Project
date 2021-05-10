import React from 'react'
import SearchIcon from '@material-ui/icons/Search';
import HomeIcon from '@material-ui/icons/Home';
import './Header.css'
import ShoppingCart from '@material-ui/icons/ShoppingCart';
import MessageIcon from '@material-ui/icons/Message';
import NotificationsIcon from '@material-ui/icons/Notifications';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';

function Header() {
    return (
        <div className='header'>
            <div
            className="header__logo">CEBERUS</div>

            <div className='header__search'>
                <input className ='header__searchInputDevice' type="text" placeholder="Device"/>
                <input className ='header__searchInputIssue' type="text" placeholder="Repair/Issue"/>
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
                <div className="header__option header__accountOption">
                    <AccountCircleIcon className="header__optionIcon"/>
                    <div className="header__optionText">Account</div>
                </div>
            </div>
        </div>
    )
}

export default Header