// Select all necessary elements
let videoList = document.querySelectorAll('.video-list-container .list');
let mainVideo = document.querySelector('.main-video-container .main-video');
let mainVideoTitle = document.querySelector('.main-video-container .main-vid-title');
let playPauseButton = document.querySelector('.play-pause-button');
let nextButton = document.querySelector('.next-button');
let prevButton = document.querySelector('.prev-button');
let forwardButton = document.querySelector('.forward-button');
let backwardButton = document.querySelector('.backward-button');
let volumeBar = document.querySelector('.volume-bar');
let volumeIcon = document.querySelector('.volume-icon');

let currentIndex = 0;

let isMuted = false;

// // Function to handle adding a new video to the list
// // Function to handle adding a new video to the list
// function addVideoToList() {
//    let videoFile = document.getElementById('videoFile').files[0];
//    let videoTitle = document.getElementById('videoTitle').value;

//    if (!videoFile || !videoTitle.trim()) {
//        alert('Please select a video file and enter a title');
//        return;
//    }

//    let reader = new FileReader();
//    reader.onload = function(event) {
//        let newVideo = document.createElement('div');
//        newVideo.classList.add('list');
//        newVideo.innerHTML = `
//            <video src="${event.target.result}" class="list-video"></video>
//            <h3 class="list-title">${videoTitle}</h3>
//        `;

//        newVideo.querySelector('video').onclick = () => {
//            let index = Array.from(newVideo.parentElement.children).indexOf(newVideo);
//            playVideo(index);
//        };

//        document.querySelector('.video-list-container').appendChild(newVideo);
//    };
//    reader.readAsDataURL(videoFile);

//    document.getElementById('videoTitle').value = '';
// }

// // Click event listener for add video button
// document.getElementById('addVideoButton').onclick = addVideoToList;


// Event listener for keydown event
document.addEventListener('keydown', (event) => {
    // Play/pause video when space bar is pressed
    if (event.code === 'Space') {
        if (mainVideo.paused) {
            mainVideo.play();
            playPauseButton.textContent = 'Pause';
        } else {
            mainVideo.pause();
            playPauseButton.textContent = 'Play';
        }
    }
    
    // Play next video when right arrow is pressed
    if (event.code === 'ArrowRight') {
        currentIndex = (currentIndex + 1) % videoList.length;
        playVideo(currentIndex);
    }
    
    // Play previous video when left arrow is pressed
    if (event.code === 'ArrowLeft') {
        currentIndex = (currentIndex - 1 + videoList.length) % videoList.length;
        playVideo(currentIndex);
    }
    
    // Increase volume when up arrow is pressed
    // Increase volume when up arrow is pressed
    if (event.code === 'ArrowUp') {
        mainVideo.volume = Math.min(mainVideo.volume + 0.1, 1);
        updateVolumeIcon();
        volumeBar.value = mainVideo.volume;
    }
    
    // Decrease volume when down arrow is pressed
    if (event.code === 'ArrowDown') {
        mainVideo.volume = Math.max(mainVideo.volume - 0.1, 0);
        updateVolumeIcon();
        volumeBar.value = mainVideo.volume;
    }
});




// Function to play the selected video
function playVideo(index) {
    videoList.forEach(remove => {
        remove.classList.remove('active')
    });
    videoList[index].classList.add('active');
    let src = videoList[index].querySelector('.list-video').src;
    let title = videoList[index].querySelector('.list-title').innerHTML;
    mainVideo.src = src;
    mainVideo.play();
    mainVideoTitle.innerHTML = title;
    currentIndex = index;
}

// Click event listener for each video list item
videoList.forEach((vid, index) => {
    vid.onclick = () => {
        playVideo(index);
    };
});

// Click event listener for play/pause button
playPauseButton.onclick = () => {
    if (mainVideo.paused) {
        mainVideo.play();
        playPauseButton.textContent = 'Pause';
    } else {
        mainVideo.pause();
        playPauseButton.textContent = 'Play';
    }
};

// Click event listener for next button
nextButton.onclick = () => {
    currentIndex = (currentIndex + 1) % videoList.length;
    playVideo(currentIndex);
};

// Click event listener for previous button
prevButton.onclick = () => {
    currentIndex = (currentIndex - 1 + videoList.length) % videoList.length;
    playVideo(currentIndex);
};


// Click event listener for forward button
forwardButton.onclick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    mainVideo.currentTime += 10;
};

// Click event listener for backward button
backwardButton.onclick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    mainVideo.currentTime -= 10;
};


// Event listener for volume bar
volumeBar.oninput = () => {
   mainVideo.volume = volumeBar.value;
   updateVolumeIcon();
};

// Click event listener for volume icon
volumeIcon.onclick = () => {
   isMuted = !isMuted;
   if (isMuted) {
       mainVideo.muted = true;
       volumeIcon.textContent = '🔇';
   } else {
       mainVideo.muted = false;
       updateVolumeIcon();
   }
};

// Function to update volume icon based on volume level
function updateVolumeIcon() {
   if (mainVideo.volume === 0) {
       volumeIcon.textContent = '🔇';
   } else if (mainVideo.volume < 0.5) {
       volumeIcon.textContent = '🔉';
   } else {
       volumeIcon.textContent = '🔊';
   }
}



