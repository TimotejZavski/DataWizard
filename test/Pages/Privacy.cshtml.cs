using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.IO;

namespace test.Pages
{
    public class PrivacyModel : PageModel
    {
        public string[] ImageUrls { get; private set; }

        private readonly ILogger<PrivacyModel> _logger;

        public PrivacyModel(ILogger<PrivacyModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
            // Specify the path to the folder where your .png files are stored
            string folderPath = "/Users/timzav/Desktop/test";
            string[] imageFiles = Directory.GetFiles(folderPath, "*.png");

            // Generate absolute URLs for the images
            ImageUrls = new string[imageFiles.Length];
            for (int i = 0; i < imageFiles.Length; i++)
            {
                // Use Url.Content to generate absolute URLs
                ImageUrls[i] = Url.Content("~/Images/" + Path.GetFileName(imageFiles[i]));
            }
        }
    }
}
