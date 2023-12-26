using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.IO;
using System.Threading.Tasks;
using CsvHelper;
using Newtonsoft.Json;
using System.Globalization;
using Python.Runtime;


namespace test.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        [BindProperty]
        public IFormFile? Upload { get; set; }

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
            // Your existing code for the GET request
            
        }
        [BindProperty]
        public string Description { get; set; }

        [BindProperty]
        public string Task { get; set; }

        public async Task<IActionResult> OnPostUploadFileAsync()
        {
// Upload
            if (Upload != null && Upload.Length > 0)
            {

                var filePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "uploads", Upload.FileName);

                using (var stream = new FileStream(filePath, FileMode.Create))
                {
                    await Upload.CopyToAsync(stream);
                }

                TempData["Message"] = "<span style='color: #30db5b;'>SUCCESS:</span> File, description, and task Uploaded!";

         // Convert CSV to JSON
                var csvFilePath = filePath;  // Assuming Uploaded file is a CSV
                var jsonFilePath = Path.ChangeExtension(filePath, ".json");  // Change extension to .json

                using (var reader = new StreamReader(csvFilePath))
                using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
                {
                    var records = csv.GetRecords<dynamic>().ToList();

                    // Serialize to JSON
                    var json = JsonConvert.SerializeObject(records, Formatting.Indented);

                    // Write JSON to file
                    System.IO.File.WriteAllText(jsonFilePath, json);
                }

                string inputs = $"Description: {Description}, Task: {Task}";

                var python = Python.CreateRuntime();

                python.SetVariable("json_file_path", jsonFilePath);
                python.SetVariable("inputs", inputs);

                // run script
                var scriptPath = "/Users/timzav/Desktop/test/im.py";
                python.ExecuteFile(scriptPath);



            }
            else
            {
                TempData["Message"] = "<span style='color: #ff6961;'>ERROR:</span>ERROR: File, description, or task not uploaded!";
            }

            // Redirect back to the index page after the file is uploaded
            return RedirectToPage("/Index");
        }
    }
}
