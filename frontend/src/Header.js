import React from 'react'
import SearchIcon from '@material-ui/icons/Search';
import './Header.css'

function Header() {
    return (
        <div className='header'>
            <img 
            className="header__logo"
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1000px-Amazon_logo.svg.png"></img>

            <div className='header__search'>
                <input className ='header_searchInput' type="text"/>
                <SearchIcon/>
            </div>

            {/* Logo */}

            <div className='header__nav'>
                <div className="header__option">
                    Home
                </div>
                <div className="header__option">
                    Orders
                </div>
                <div className="header__option">
                    Messaging
                </div>
                <div className="header__option">
                    Notifications
                </div>
            </div>
        </div>
    )
}

export default Header
