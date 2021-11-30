// variables

// ! link to home
const mainPage = document.getElementById("main-page")

// ! link to homepage cards
const subPage1 = document.getElementById("sub-page-1")
const subPage2 = document.getElementById("sub-page-2")
const subPage3 = document.getElementById("sub-page-3")

// ! link to about page
const aboutPage = document.getElementById("about-page")

// ! link to download
const downloadPage = document.getElementById("download-page")

// ! link to download sub page
const downloadSubPage = document.getElementById("download-sub-page")
const logo1 = document.getElementById("1")
const logo2 = document.getElementById("2")



// ! link to contacts page
const contactPage = document.getElementById("contacts-page")


// ? NAV LINKS

// home page link
const goHome = () => {
    mainPage.classList.remove('hide')

    subPage1.classList.add('hide')
    subPage2.classList.add('hide')
    subPage3.classList.add('hide')

    downloadSubPage.classList.add('hide')
   
    aboutPage.classList.add('hide')
    downloadPage.classList.add('hide')
    contactPage.classList.add('hide')

}

// Aboutpage link
const goAbout = () => {
    aboutPage.classList.remove('hide')

    subPage1.classList.add('hide')
    subPage2.classList.add('hide')
    subPage3.classList.add('hide')

    downloadSubPage.classList.add('hide')
   
    mainPage.classList.add('hide')
    downloadPage.classList.add('hide')
    contactPage.classList.add('hide')

}


// download link
const goDownload = () => {
    downloadPage.classList.remove('hide')

    subPage1.classList.add('hide')
    subPage2.classList.add('hide')
    subPage3.classList.add('hide')

    downloadSubPage.classList.add('hide')
   


    mainPage.classList.add('hide')
    aboutPage.classList.add('hide')
    contactPage.classList.add('hide')

}

// Contacts link
const goContacts = () => {
    contactPage.classList.remove('hide')

    subPage1.classList.add('hide')
    subPage2.classList.add('hide')
    subPage3.classList.add('hide')

    downloadSubPage.classList.add('hide')
  

    mainPage.classList.add('hide')
    aboutPage.classList.add('hide')
    downloadPage.classList.add('hide')

}

// ? SUB PAGES

// show sub Card pages

const showPageOne = () => {
    subPage1.classList.toggle("hide")

    subPage2.classList.add('hide')
    subPage3.classList.add('hide')
}
const showPageTwo = () => {
    subPage2.classList.toggle("hide")

    subPage1.classList.add('hide')
    subPage3.classList.add('hide')
}
const showPageThree = () => {
    subPage3.classList.toggle("hide")

    subPage1.classList.add('hide')
    subPage2.classList.add('hide')
}


// download sub link

const showDownSub = () => {
    downloadSubPage.classList.toggle("hide")
}

const slowGif = () => {

    logo1.classList.toggle("hide")
    logo2.classList.toggle("hide")
}