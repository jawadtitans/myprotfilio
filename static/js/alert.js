<script type="text/javascript">
    document.getElementById('downloadCVBtn').addEventListener('click', function() {
        // Show the alert with a countdown message
        alert('Your download will start in 5 seconds...');
        
        // After 5 seconds, trigger the download
        setTimeout(function() {
            // Redirect to the download URL
            window.location.href = "{% url 'download_cv' %}";
        }, 5000);  // 5000 milliseconds = 5 seconds
    });
</script>
