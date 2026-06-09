#ifndef EXAMPLE_CONFIG_H
#define EXAMPLE_CONFIG_H
/*!
 * @file
 * @brief This is a config file
 * @details This is a detailed description
 * @ingroup animals
 * @addtogroup animals
 * @{
 */

#define CONFIG_HELLO (123)
#define CONFIG_WORLD ("abx")
#define PI 3.14159265358979323846
#define PRINT_PRETTY(MSG, ...) printf(MSG, __VA_ARGS__)

/*!
 * @brief BSP display configuration structure
 */
struct bsp_display_cfg_t {
	int buffer_size;    /*!< Size of the buffer for the screen in pixels */
	bool double_buffer; /*!< True, if should be allocated two buffers */
	struct {
		unsigned int buff_dma: 1;    /*!< Allocated LVGL buffer will be DMA capable */
		unsigned int buff_spiram: 1; /*!< Allocated LVGL buffer will be in PSRAM */
	} flags;
};

/*! @} */
#endif
