/*=====================================
 Let´s handler this styles!$
 =====================================*/

// Colors Light
const whiteLight = '#ffffff7d';
const yellowLight = '#fcfbb370';
const greenLight = '#0d913e';
const secondManinColor = '#fff662';
const white = '#ffffff'
const grey = '#707070';
const dark = '#333'
const whats = '#47c756'
const superBlack = 'black'

const mainDj = '#ca6ff7'
const mainSocial  = secondManinColor;
const mainInst  = '#c9c8c8';

const mainLightSocial = yellowLight;
const mainLightInst = whiteLight;
const mainLightDj = '#ffc4e97d';
const mainDarkDj = '#8305547d'

const llamativoSocial = secondManinColor;
const llamativoInst = '#abab69';
const llamativoDj = '#49b095';
const djSuperContrast = '#d3cc00';

// llamativo light #49b09591
const llamativoDjLight = '#77e4ca';
const llamativoLightSocial = yellowLight;
const llamativoLightInst = whiteLight;

const llamativoDarkSocial = '#128243'
const llamativoDarkInst = 'white'
const llamativoDarkDj = '#1998ab'
const llamativoContrasteDj = '#673ab7';


let mainLight;
let mainDark;
let mainColor;
let llamativo;
let llamativoLight;
let llamativoDark;
let llamativoContraste;

let justOneColorDj;
let justOneColorSocial;
let justOneColorInst;

let justOneColorDjDark;
let justOneColorSocialDark;
let justOneColorInstDark;

// Themes
let djThemellamativo = 'inherit'
let colorTheme;
let superContrast;

// Elements
const windowsHeight = window.innerHeight;
const header = document.getElementById('header');
const mainControlersHeader = document.getElementById('mainControlersHeader');
const contactBtn = document.getElementById('contactBtn');
const mySidenavMarv = document.getElementById('mySidenavMarv');
const about = document.getElementById('about');
const faq = document.getElementById('faq');
const service = document.getElementById('service');
// Clases
const h4SubHeader = document.getElementsByClassName('subheader');

// Window Listener
window.onscroll = function() {onScroll()};

// Master Controls
function masterControl() {
  setMainElements()
    mySidenavMarv.style.left = '-60px';
}

// Scroll function
function onScroll() {
  if (document.body.scrollTop > window.innerHeight || document.documentElement.scrollTop > window.innerHeight)
    {
      console.log("Pasing!!!!")
      mySidenavMarv.style.display = 'block';
      mySidenavMarv.style.opacity = 1;
    }
    else {
      mySidenavMarv.style.display = 'none';
      mySidenavMarv.style.opacity = 0;
    }
}



// Set Colors
function setTheme(theme) {
  

    if (theme == 'social' || theme == undefined){
      mainColor = mainSocial;
      mainLight = mainLightSocial;
      mainDark = mainLightSocial;
      llamativeColor = llamativoSocial;
      llamativoLight = llamativoLightSocial;
      llamativoDark = llamativoDarkSocial;

      // Just One Colors
      justOneColorDj = white;
      justOneColorSocial = white;
      justOneColorInst = mainLightInst;
      justOneColorDjDark = grey;
      justOneColorSocialDark = llamativoDark;
      justOneColorInstDark = grey;

      backgroundColorTheme = white;
      llamativoThemeColor = dark;
      specialBackground = white;
      llamativoContraste = white;

      // For body
      colorTheme = '#777777'

    }

    if (theme == 'inst'){
      mainColor = mainInst;
      mainLight = mainLightInst;
      mainDark = white;
      llamativeColor = llamativoInst;
      llamativoLight = llamativoLightInst;
      llamativoDark = llamativoDarkInst;

      // Just One Colors
      justOneColorDj = white;
      justOneColorSocial = mainLightSocial;
      justOneColorInst = white;
      justOneColorDjDark = grey;
      justOneColorSocialDark = grey;
      justOneColorInstDark = llamativoDark;

      backgroundColorTheme = white;
      llamativoThemeColor = dark;
      specialBackground = white;
      llamativoContraste = white;

      // For body
      colorTheme = '#777777'

    }

    if (theme == 'dj'){

      mainColor = mainDj;
      mainLight = mainLightDj;
      mainDark = mainDarkDj;
      llamativeColor = llamativoDj;
      llamativoLight = llamativoDjLight;
      llamativoDark = llamativoDarkDj;

      // Just One Colors
      justOneColorDj = mainLight;
      justOneColorSocial = white;
      justOneColorInst = white;
      justOneColorDjDark = '#ffe83c';
      justOneColorSocialDark = grey;
      justOneColorInstDark = grey;

      djThemellamativo = llamativoDj;

      // theme
      backgroundColorTheme = dark;
      llamativoThemeColor = llamativoDj;
      specialBackground = superBlack;
      llamativoContraste = llamativoContrasteDj;

      // For body
      colorTheme = llamativoDjLight



    }




    /**********************************************************
        Colors
    */

    // Set Boy Color
    document.body.style.backgroundColor = backgroundColorTheme;
    document.body.style.color = colorTheme;

    // Set header color
    header.style.backgroundColor = mainLight;

    // Set about color (justo for dj_)
    about.style.background = specialBackground;
    faq.style.background = specialBackground;
    service.style.background = specialBackground;


    // Set h4 sub header color
    for(var i =0; i < h4SubHeader.length; i++ ) {
      if ( theme == 'dj')
        h4SubHeader[i].style.setProperty('color', llamativoDjLight, 'important');
      else
        h4SubHeader[i].style.setProperty('color', mainLight, 'important');
    }

    // Icons
    document.documentElement.style.setProperty('--djOneColor', justOneColorDj);
    document.documentElement.style.setProperty('--socialOneColor', justOneColorSocial);
    document.documentElement.style.setProperty('--instOneColor', justOneColorInst);
    document.documentElement.style.setProperty('--djOneColorDark', justOneColorDjDark);
    document.documentElement.style.setProperty('--socialOneColorDark', justOneColorSocialDark);
    document.documentElement.style.setProperty('--instOneColorDark', justOneColorInstDark);
    document.documentElement.style.setProperty('--llamativoInst', llamativoInst);
    document.documentElement.style.setProperty('--llamativoSocial', llamativoSocial);
    document.documentElement.style.setProperty('--llamativoDj', llamativoDj);

    // All llamativo Colors
    document.documentElement.style.setProperty('--mainColor', mainColor);
    document.documentElement.style.setProperty('--mainLight', mainLight);
    document.documentElement.style.setProperty('--llamativo', llamativeColor);
    document.documentElement.style.setProperty('--llamativoDark', llamativoDark);
    document.documentElement.style.setProperty('--llamativoContraste', llamativoContraste);
    // Colors
    document.documentElement.style.setProperty('--marvGrey', grey);
    document.documentElement.style.setProperty('--whats', whats);

    // Themes
    document.documentElement.style.setProperty('--llamativoThemeColor', llamativoThemeColor);
    document.documentElement.style.setProperty('--mainDark', mainDark);
    document.documentElement.style.setProperty('--superContrast', superContrast);

}

function setMainElements () {
    // Just Vars
    let mCHeaderHeight;

    /**********************************************************
        Proportions
    */

    // Main Controls Header
    mCHeaderHeight = (windowsHeight - mainControlersHeader.offsetHeight) * .90
    //mainControlersHeader.style.top = mCHeaderHeight + 'px';

}
